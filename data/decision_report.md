# Decision Report

- generated_at: 2026-10-01T15:56:50.892273+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15920**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15920, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.48% | **-1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.24% | **+0.56%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.63% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.53% | **+1.64%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.10% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,297.67** / 初期 $100.00 (+1197.67%)
- 確定: 6029件 (Win 1786 / Loss 1941 / Flat 2302) / skip 6452件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,297.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.20** / 初期 $100.00 (+178.20%)
- 確定: 3573件 (Win 995 / Loss 825 / Flat 1753) / skip 5758件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1557 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $278.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4085件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000388 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T15:56:35.977252+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=84080.1
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1, 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +79.81% | $8,869,827.90 |
| MOVR/USDT:USDT | +69.61% | $22,447,797.99 |
| CAP/USDT:USDT | +30.86% | $1,360,063.57 |
| US/USDT:USDT | +29.97% | $1,474,555.04 |
| ALICE/USDT:USDT | +26.11% | $1,471,550.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +4.06% | +3.98% |
| LITESTOCK/USDT:USDT | below_1h_threshold | +4.04% | +3.96% |
| ALICE/USDT:USDT | below_1h_threshold | +3.44% | +3.35% |
| JASMY/USDT:USDT | below_1h_threshold | +2.92% | +2.83% |
| MONAD/USDT:USDT | below_1h_threshold | +2.47% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
