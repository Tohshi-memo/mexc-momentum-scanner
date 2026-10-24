# Decision Report

- generated_at: 2026-10-24T09:16:21.220770+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17348**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17348, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.86% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.27% | **+1.15%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.36% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,316.03** / 初期 $100.00 (+1216.03%)
- 確定: 6601件 (Win 1909 / Loss 2103 / Flat 2589) / skip 7308件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,316.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3930件 (Win 1083 / Loss 920 / Flat 1927) / skip 6829件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0928 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5506件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000246 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T09:16:08.715491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80610.3
- Funnel: target 1079 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORDER/USDT:USDT | +124.19% | $1,073,942.65 |
| BIRB/USDT:USDT | +67.39% | $12,155,657.18 |
| BMT/USDT:USDT | +63.98% | $2,081,517.89 |
| IN/USDT:USDT | +21.89% | $1,010,468.16 |
| IRYS/USDT:USDT | +19.54% | $103,129,647.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +2.88% | +2.96% |
| LUNC/USDT:USDT | below_1h_threshold | +0.66% | +0.74% |
| NIL/USDT:USDT | below_1h_threshold | +0.56% | +0.64% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.43% | +0.51% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.35% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
