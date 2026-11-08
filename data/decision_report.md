# Decision Report

- generated_at: 2026-11-08T23:36:21.546184+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18494**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=18494, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.60% | **+0.51%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.28% | **+0.39%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.68% | **+0.27%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.98%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7161件 (Win 2057 / Loss 2285 / Flat 2819) / skip 7894件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4756件 (Win 1277 / Loss 1047 / Flat 2432) / skip 7149件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.0863 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_10PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6652件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T23:36:08.455567+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.02% price=75192.0
- Funnel: target 1089 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +18.46% | $59,065,081.17 |
| AIOT/USDT:USDT | +8.11% | $6,145,770.37 |
| SOXS/USDT:USDT | +3.80% | $5,585,049.31 |
| BTW/USDT:USDT | +1.92% | $5,596,597.10 |
| BLESS/USDT:USDT | +1.71% | $1,055,750.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USOIL/USDT:USDT | below_1h_threshold | +2.22% | +1.20% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.22% | +1.20% |
| SOXS/USDT:USDT | below_1h_threshold | +2.00% | +0.98% |
| PONS/USDT:USDT | below_1h_threshold | +1.87% | +0.85% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.69% | +0.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
