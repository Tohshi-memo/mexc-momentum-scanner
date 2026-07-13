# Decision Report

- generated_at: 2026-07-13T00:36:07.485105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8619**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.10% / filled 20/20。**
- 全期間 MARKET基準: n=8619, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.83% | **+1.65%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.93% | **+1.54%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.91% | **+0.64%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.58% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.25% | **+0.25%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.21% | **+0.18%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.17% | **+0.13%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | -0.11% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.20** / 初期 $100.00 (+1.20%)
- 確定トレード: 91件 (TP 30 / SL 59 / EXP 2)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.39** / 初期 $100.00 (+221.39%)
- 確定: 2792件 (Win 876 / Loss 923 / Flat 993) / skip 2388件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLAST/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $321.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1385件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 61件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000475 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-13T00:36:01.566185+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=64080.1
- Funnel: target 863 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +40.61% | $4,090,509.32 |
| ANSEM/USDT:USDT | +17.83% | $4,303,933.69 |
| BLAST/USDT:USDT | +11.75% | $1,906,464.91 |
| BILL/USDT:USDT | +5.26% | $10,332,944.04 |
| PIPPIN/USDT:USDT | +4.31% | $7,602,088.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_relative_strength | +5.21% | +4.70% |
| BILL/USDT:USDT | below_1h_threshold | +4.86% | +4.34% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.78% | +3.26% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.43% | +2.91% |
| PYTH/USDT:USDT | below_1h_threshold | +2.69% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
