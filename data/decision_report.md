# Decision Report

- generated_at: 2026-11-02T07:21:14.680307+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18015**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.95% / filled 20/20。**
- 全期間 MARKET基準: n=18015, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.37% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.84% | **+0.80%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_BB3S | 3/18 | 16.7% | +3.54% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.82% | **+4.82%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,530.01** / 初期 $100.00 (+1430.01%)
- 確定: 6867件 (Win 1991 / Loss 2203 / Flat 2673) / skip 7709件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,530.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.86** / 初期 $100.00 (+281.86%)
- 確定: 4455件 (Win 1194 / Loss 988 / Flat 2273) / skip 6971件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0881 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $381.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000264 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T07:21:04.181896+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78149.9
- Funnel: target 1088 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +43.88% | $2,358,325.27 |
| IDOL/USDT:USDT | +28.71% | $15,249,910.53 |
| EVAA/USDT:USDT | +17.84% | $7,223,228.24 |
| RT/USDT:USDT | +13.17% | $1,643,492.05 |
| KORU/USDT:USDT | +9.51% | $31,652,662.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RT/USDT:USDT | below_1h_threshold | +2.26% | +2.24% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.07% | +2.05% |
| EVAA/USDT:USDT | below_1h_threshold | +2.05% | +2.03% |
| UNITREE/USDT:USDT | below_1h_threshold | +0.79% | +0.77% |
| TRX/USDT:USDT | below_1h_threshold | +0.53% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
