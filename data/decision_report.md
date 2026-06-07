# Decision Report

- generated_at: 2026-06-07T19:10:45.007079+00:00
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

- 更新: 2026-06-07T19:10:42.091876+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.65% price=61595.4
- Funnel: target 768 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +21.50% | $3,007,788.71 |
| EPIC/USDT:USDT | +12.69% | $1,099,723.43 |
| BTW/USDT:USDT | +8.35% | $14,288,718.89 |
| BEAT/USDT:USDT | +7.18% | $51,948,076.41 |
| BABY/USDT:USDT | +6.36% | $3,268,822.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +4.95% | +5.60% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.56% | +4.21% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.59% | +2.24% |
| USOIL/USDT:USDT | below_1h_threshold | +1.51% | +2.16% |
| EDEN/USDT:USDT | below_1h_threshold | +0.47% | +1.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
