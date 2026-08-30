# Decision Report

- generated_at: 2026-08-30T03:11:19.886750+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13000**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13000, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.95% | **+1.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$788.10** / 初期 $100.00 (+688.10%)
- 確定: 4770件 (Win 1455 / Loss 1569 / Flat 1746) / skip 4791件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $788.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.68** / 初期 $100.00 (+72.68%)
- 確定: 2084件 (Win 582 / Loss 505 / Flat 997) / skip 4327件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1198 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $172.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.34** / 初期 $100.00 (+16.34%)
- 確定: 2048件 (Win 602 / Loss 796 / Flat 650) / pending 4件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000534 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DOS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.34

## 6. Latest Market Context

- 更新: 2026-08-30T03:11:11.934787+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78061.5
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +68.32% | $1,652,189.95 |
| FONE/USDT:USDT | +49.72% | $1,268,377.27 |
| PONS/USDT:USDT | +39.80% | $1,383,749.63 |
| PROM/USDT:USDT | +34.25% | $13,393,505.36 |
| HNT/USDT:USDT | +28.25% | $26,435,340.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.24% | +4.25% |
| PONS/USDT:USDT | below_1h_threshold | +4.00% | +4.02% |
| FONE/USDT:USDT | below_1h_threshold | +3.15% | +3.17% |
| 4/USDT:USDT | below_1h_threshold | +1.74% | +1.76% |
| O/USDT:USDT | below_1h_threshold | +1.49% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
