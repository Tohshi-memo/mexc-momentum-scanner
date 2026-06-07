# Decision Report

- generated_at: 2026-06-07T19:16:40.209623+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5993**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5993, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| ASK | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.69% | **+3.79%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.62** / 初期 $100.00 (+49.62%)
- 確定: 1110件 (Win 268 / Loss 334 / Flat 508) / skip 1444件
- 成長率目線: 平均log +0.000363 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $149.62

## 4. Latest Market Context

- 更新: 2026-06-07T19:16:37.357055+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.94% price=61415.9
- Funnel: target 768 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +22.74% | $3,047,212.61 |
| EPIC/USDT:USDT | +12.51% | $1,111,425.96 |
| BTW/USDT:USDT | +8.81% | $14,335,988.55 |
| BEAT/USDT:USDT | +7.72% | $52,997,163.11 |
| BABY/USDT:USDT | +6.68% | $3,287,479.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.25% | +5.19% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.61% | +2.55% |
| USOIL/USDT:USDT | below_1h_threshold | +1.46% | +2.40% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.98% | +1.92% |
| MYX/USDT:USDT | below_1h_threshold | +0.87% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
