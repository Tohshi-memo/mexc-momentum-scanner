# Decision Report

- generated_at: 2026-05-25T08:29:16.895298+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4852**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4852, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

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
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.34% | **+2.50%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.99% | **+1.59%** |
| MARKET_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.90% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.65** / 初期 $100.00 (+27.65%)
- 確定: 658件 (Win 165 / Loss 206 / Flat 287) / skip 755件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.91% 残高後 $127.65

## 4. Latest Market Context

- 更新: 2026-05-25T08:29:14.559270+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77286.4
- Funnel: target 764 → liquid 117 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +39.91% | $5,912,098.31 |
| XAN/USDT:USDT | +39.63% | $5,484,647.33 |
| SAGA/USDT:USDT | +17.32% | $1,615,923.25 |
| PHA/USDT:USDT | +13.24% | $1,325,511.19 |
| H/USDT:USDT | +12.62% | $1,393,352.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.61% | +3.72% |
| PLAY/USDT:USDT | below_1h_threshold | +1.79% | +1.90% |
| BILL/USDT:USDT | below_1h_threshold | +1.53% | +1.64% |
| NIL/USDT:USDT | below_1h_threshold | +1.36% | +1.47% |
| H/USDT:USDT | below_1h_threshold | +0.84% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
