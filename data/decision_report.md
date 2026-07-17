# Decision Report

- generated_at: 2026-07-17T10:01:09.927853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8838**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.78% / filled 20/20。**
- 全期間 MARKET基準: n=8838, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.33% | **+1.13%** |
| LIMIT_BB3S | 5/15 | 33.3% | +2.98% | **+0.99%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.97% | **+0.79%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.25% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.18% | **+0.24%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.21% | **-0.07%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.11% | **-0.08%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.17% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$111.81** / 初期 $100.00 (+11.81%)
- 確定トレード: 111件 (TP 42 / SL 65 / EXP 4)
- 最新: DODO/USDT:USDT TP_HIT PnL +8.00% 残高後 $111.81
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$343.23** / 初期 $100.00 (+243.23%)
- 確定: 2953件 (Win 919 / Loss 947 / Flat 1087) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LRC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $343.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.10** / 初期 $100.00 (+8.10%)
- 確定: 800件 (Win 186 / Loss 171 / Flat 443) / skip 1449件
- 成長率目線: 平均log +0.000097 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0296 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $108.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.51** / 初期 $100.00 (-1.49%)
- 確定: 105件 (Win 33 / Loss 68 / Flat 4) / pending 3件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LRC/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.51

## 6. Latest Market Context

- 更新: 2026-07-17T10:01:03.592677+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62971.3
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XEC/USDT:USDT | +27.18% | $1,210,200.32 |
| LUMIA/USDT:USDT | +25.10% | $2,526,762.23 |
| LRC/USDT:USDT | +19.38% | $1,658,533.48 |
| AKE/USDT:USDT | +17.62% | $41,411,782.72 |
| BANK/USDT:USDT | +17.14% | $5,868,909.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APDSTOCK/USDT:USDT | below_1h_threshold | +1.20% | +1.18% |
| VELVET/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |
| JASMY/USDT:USDT | below_1h_threshold | +0.71% | +0.69% |
| USOIL/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.39% | +0.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
