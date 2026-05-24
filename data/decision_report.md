# Decision Report

- generated_at: 2026-05-24T14:09:05.403289+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4824**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4824, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.03% | **+0.15%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.42% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.08% | **+2.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.19% | **+1.75%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.03% | **+1.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.92% | **+1.31%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 630件 (Win 156 / Loss 199 / Flat 275) / skip 755件
- 成長率目線: 平均log +0.000335 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $123.52

## 4. Latest Market Context

- 更新: 2026-05-24T14:09:03.264623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=76712.3
- Funnel: target 764 → liquid 114 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +65.00% | $4,953,703.88 |
| NIL/USDT:USDT | +23.21% | $4,653,665.00 |
| UB/USDT:USDT | +21.28% | $2,648,336.61 |
| GRASS/USDT:USDT | +19.29% | $10,990,549.89 |
| GENIUS/USDT:USDT | +19.09% | $5,285,103.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.11% | +3.18% |
| PLAY/USDT:USDT | below_1h_threshold | +1.47% | +1.54% |
| BAN/USDT:USDT | below_1h_threshold | +1.26% | +1.33% |
| VVV/USDT:USDT | below_1h_threshold | +1.09% | +1.16% |
| NEAR/USDT:USDT | below_1h_threshold | +0.67% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
