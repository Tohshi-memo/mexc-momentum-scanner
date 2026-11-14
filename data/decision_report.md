# Decision Report

- generated_at: 2026-11-14T15:26:19.009316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18908**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18908, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.64% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +6.40% | **+1.60%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.90% | **+1.45%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.47% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,731.41** / 初期 $100.00 (+1631.41%)
- 確定: 7312件 (Win 2103 / Loss 2344 / Flat 2865) / skip 8157件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,731.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$425.50** / 初期 $100.00 (+325.50%)
- 確定: 4916件 (Win 1314 / Loss 1080 / Flat 2522) / skip 7403件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0917 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $425.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7067件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T15:26:06.226803+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.01% price=65227.4
- Funnel: target 1071 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +61.79% | $3,005,126.75 |
| AKE/USDT:USDT | +23.59% | $82,572,236.63 |
| SHELL/USDT:USDT | +22.74% | $5,427,561.85 |
| DODO/USDT:USDT | +14.33% | $2,033,822.46 |
| NIGHT/USDT:USDT | +11.85% | $2,596,614.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.34% | +2.35% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.62% | +1.63% |
| SOXL/USDT:USDT | below_1h_threshold | +0.39% | +1.40% |
| UVXY/USDT:USDT | below_1h_threshold | +0.11% | +1.11% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +0.05% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
