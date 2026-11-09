# Decision Report

- generated_at: 2026-11-09T14:11:26.606676+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18528**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18528, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.05% | **+0.79%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_BB3S | 4/13 | 30.8% | +1.52% | **+0.47%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.54% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +3.14% | **+2.35%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.36% | **+1.89%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.13% | **+1.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.39% | **+1.54%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.45% | **+1.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 266件 (TP 97 / SL 161 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7163件 (Win 2057 / Loss 2285 / Flat 2821) / skip 7926件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RITUAL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4757件 (Win 1277 / Loss 1047 / Flat 2433) / skip 7182件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T14:11:12.814885+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=74499.3
- Funnel: target 1094 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +23.06% | $3,734,644.63 |
| PIEVERSE/USDT:USDT | +20.17% | $2,735,274.85 |
| EDGE/USDT:USDT | +17.41% | $1,073,996.10 |
| RITUAL/USDT:USDT | +16.48% | $1,668,770.79 |
| IDOL/USDT:USDT | +11.36% | $2,207,099.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.63% | +2.89% |
| DELTAELECSTOCK/USDT:USDT | below_1h_threshold | +1.68% | +1.94% |
| NGAS/USDT:USDT | below_1h_threshold | +1.37% | +1.63% |
| EDGE/USDT:USDT | below_1h_threshold | +1.33% | +1.59% |
| PEPE/USDT:USDT | below_1h_threshold | +0.86% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
