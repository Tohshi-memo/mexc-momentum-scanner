# Decision Report

- generated_at: 2026-11-08T16:36:28.098276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18466**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18466, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.38% | **-2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_9PCT | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_8PCT | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_7PCT | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +4.64% | **+3.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +4.52% | **+2.93%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.32% | **+2.82%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.31% | **+2.49%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +6.18% | **+1.55%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,675.79** / 初期 $100.00 (+1575.79%)
- 確定: 7150件 (Win 2057 / Loss 2279 / Flat 2814) / skip 7877件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.04% 残高後 $1,675.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7122件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_10PCT` (selected_by_robust_growth_score) / robust_score +0.1698 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6628件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000503 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T16:36:14.958457+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=75991.7
- Funnel: target 1089 → liquid 103 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1, 4h RSI 81.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +11.39% | $4,023,474.60 |
| JCT/USDT:USDT | +5.58% | $28,782,571.04 |
| CLAUDIA/USDT:USDT | +3.88% | $15,354,036.65 |
| KOMA/USDT:USDT | +1.85% | $1,232,763.05 |
| HOT/USDT:USDT | +1.74% | $5,009,265.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +3.88% | +3.95% |
| KOMA/USDT:USDT | below_1h_threshold | +1.94% | +2.00% |
| HOT/USDT:USDT | below_1h_threshold | +1.75% | +1.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.34% | +1.40% |
| Q/USDT:USDT | below_1h_threshold | +1.31% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
