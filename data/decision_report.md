# Decision Report

- generated_at: 2026-06-04T15:28:23.769307+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5638**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5638, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/14 | 35.7% | +2.58% | **+0.92%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.62% | **+1.62%** |
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 97件 (TP 30 / SL 64 / EXP 3)
- 最新: HEI/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1192件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T15:28:18.494580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64003.3
- Funnel: target 772 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEST/USDT:USDT | +80.99% | $2,675,407.04 |
| OPN/USDT:USDT | +37.93% | $45,000,016.32 |
| EPIC/USDT:USDT | +35.29% | $7,175,559.97 |
| HEI/USDT:USDT | +25.67% | $5,036,039.66 |
| SIREN/USDT:USDT | +23.30% | $9,974,417.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPN/USDT:USDT | below_1h_threshold | +4.64% | +4.51% |
| ZEST/USDT:USDT | below_1h_threshold | +3.42% | +3.30% |
| EPIC/USDT:USDT | below_1h_threshold | +3.41% | +3.29% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.83% | +2.71% |
| APPSTOCK/USDT:USDT | below_1h_threshold | +1.72% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
