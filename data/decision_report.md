# Decision Report

- generated_at: 2026-11-02T20:26:30.908616+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18032**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=18032, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.44% | **+0.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.00% | **+0.70%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.71% | **+1.35%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.37% | **+1.07%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.01% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,550.82** / 初期 $100.00 (+1450.82%)
- 確定: 6884件 (Win 1997 / Loss 2208 / Flat 2679) / skip 7709件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,550.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$385.26** / 初期 $100.00 (+285.26%)
- 確定: 4472件 (Win 1201 / Loss 995 / Flat 2276) / skip 6971件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0251 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $385.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000162 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T20:26:17.750826+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77130.3
- Funnel: target 1093 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +15.88% | $1,753,626.59 |
| SOXS/USDT:USDT | +9.61% | $19,604,142.53 |
| HOT/USDT:USDT | +6.78% | $3,519,071.73 |
| JCT/USDT:USDT | +4.86% | $2,079,733.47 |
| SQQQ/USDT:USDT | +4.68% | $1,401,723.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOT/USDT:USDT | below_1h_threshold | +4.14% | +4.06% |
| AGT/USDT:USDT | below_1h_threshold | +3.76% | +3.67% |
| AIN/USDT:USDT | below_1h_threshold | +1.85% | +1.77% |
| SOXS/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |
| LYN/USDT:USDT | below_1h_threshold | +1.57% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
