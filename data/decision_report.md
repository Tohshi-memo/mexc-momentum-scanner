# Decision Report

- generated_at: 2026-08-26T12:01:30.014043+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12702, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 8/18 | 44.4% | +1.72% | **+0.76%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.56% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.87% | **+1.22%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.15% | **+0.98%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.93% | **+0.51%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.81% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$704.00** / 初期 $100.00 (+604.00%)
- 確定: 4602件 (Win 1400 / Loss 1512 / Flat 1690) / skip 4661件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $704.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.72** / 初期 $100.00 (+58.72%)
- 確定: 1997件 (Win 544 / Loss 479 / Flat 974) / skip 4116件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1273 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $158.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 1974件 (Win 580 / Loss 751 / Flat 643) / pending 6件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-08-26T12:01:23.405810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78485.5
- Funnel: target 1023 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +258.23% | $17,201,137.83 |
| TAC/USDT:USDT | +53.70% | $7,157,194.83 |
| BMT/USDT:USDT | +52.19% | $15,659,894.40 |
| LONGXIA/USDT:USDT | +28.89% | $1,986,583.60 |
| BICO/USDT:USDT | +21.29% | $2,601,961.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +0.85% | +0.80% |
| CASHCAT/USDT:USDT | below_1h_threshold | +0.85% | +0.79% |
| BLESS/USDT:USDT | below_1h_threshold | +0.40% | +0.35% |
| UNITREE/USDT:USDT | below_1h_threshold | +0.38% | +0.33% |
| BMT/USDT:USDT | below_1h_threshold | +0.37% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
