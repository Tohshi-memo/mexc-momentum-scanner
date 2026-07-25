# Decision Report

- generated_at: 2026-07-25T16:06:18.970415+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9526**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9526, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +2.32% | **+0.77%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.41% | **+1.93%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.67% | **+1.73%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.77% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$441.81** / 初期 $100.00 (+341.81%)
- 確定: 3354件 (Win 1061 / Loss 1087 / Flat 1206) / skip 2733件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHIB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $441.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$134.75** / 初期 $100.00 (+34.75%)
- 確定: 1179件 (Win 321 / Loss 257 / Flat 601) / skip 1758件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1498 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHIB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $134.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.68** / 初期 $100.00 (+7.68%)
- 確定: 573件 (Win 194 / Loss 220 / Flat 159) / pending 6件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000524 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHIB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.68

## 6. Latest Market Context

- 更新: 2026-07-25T16:06:12.087236+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64159.1
- Funnel: target 898 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +5.48% | $132,312,797.41 |
| ALLO/USDT:USDT | +2.23% | $14,353,893.03 |
| SHIB/USDT:USDT | +1.68% | $6,969,343.78 |
| RIF/USDT:USDT | +1.12% | $3,692,246.56 |
| VELVET/USDT:USDT | +1.03% | $6,593,023.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +2.48% | +2.46% |
| SHIB/USDT:USDT | below_1h_threshold | +1.62% | +1.61% |
| RIF/USDT:USDT | below_1h_threshold | +1.17% | +1.16% |
| VELVET/USDT:USDT | below_1h_threshold | +1.06% | +1.05% |
| EUL/USDT:USDT | below_1h_threshold | +0.96% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
