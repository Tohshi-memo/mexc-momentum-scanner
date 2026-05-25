# Decision Report

- generated_at: 2026-05-25T11:49:19.501558+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4854**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4854, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.95% | **-1.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.19% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.40% | **+0.36%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +6.65% | **+4.98%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.54% | **+2.12%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.23% | **+1.94%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.39% | **+1.79%** |
| MARKET_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.93** / 初期 $100.00 (+28.93%)
- 確定: 660件 (Win 166 / Loss 206 / Flat 288) / skip 755件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $128.93

## 4. Latest Market Context

- 更新: 2026-05-25T11:49:14.761383+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=77389.5
- Funnel: target 764 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +51.57% | $10,279,029.90 |
| XAN/USDT:USDT | +31.76% | $6,825,475.01 |
| SAGA/USDT:USDT | +31.75% | $2,940,169.59 |
| SPORTFUN/USDT:USDT | +19.78% | $1,440,094.64 |
| ERA/USDT:USDT | +16.33% | $1,129,616.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.68% | +3.82% |
| SAGA/USDT:USDT | below_1h_threshold | +2.78% | +2.93% |
| PLAY/USDT:USDT | below_1h_threshold | +2.18% | +2.32% |
| BILL/USDT:USDT | below_1h_threshold | +1.99% | +2.14% |
| ZEN/USDT:USDT | below_1h_threshold | +1.63% | +1.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
