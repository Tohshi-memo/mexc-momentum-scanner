# Decision Report

- generated_at: 2026-11-10T10:51:24.643131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18595**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18595, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.44% | **+1.71%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.80% | **+0.99%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.17% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,676.44** / 初期 $100.00 (+1576.44%)
- 確定: 7192件 (Win 2068 / Loss 2296 / Flat 2828) / skip 7964件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account -0.33% 残高後 $1,676.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$394.61** / 初期 $100.00 (+294.61%)
- 確定: 4761件 (Win 1280 / Loss 1048 / Flat 2433) / skip 7245件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0561 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $394.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6753件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000350 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T10:51:11.887523+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=74205.2
- Funnel: target 1094 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +51.96% | $14,430,193.67 |
| ONE/USDT:USDT | +35.71% | $7,803,653.24 |
| NIUBI/USDT:USDT | +19.19% | $2,418,879.48 |
| ARIA/USDT:USDT | +10.61% | $1,303,297.92 |
| ZHIPUSTOCK/USDT:USDT | +9.40% | $1,539,567.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +1.98% | +2.35% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.70% | +2.08% |
| HOT/USDT:USDT | below_1h_threshold | +1.19% | +1.57% |
| BR/USDT:USDT | below_1h_threshold | +0.83% | +1.20% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.76% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
