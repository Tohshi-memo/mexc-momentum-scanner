# Decision Report

- generated_at: 2026-07-18T14:41:16.189914+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8949**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8949, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.30% | **-1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.20% | **+0.66%** |
| LIMIT_BB3S | 2/12 | 16.7% | +3.73% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.99% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.85% | **+1.92%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.52% | **+1.76%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.20% | **+1.54%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.08% | **+1.14%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.91% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2461件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.56** / 初期 $100.00 (+12.56%)
- 確定: 910件 (Win 220 / Loss 184 / Flat 506) / skip 1450件
- 成長率目線: 平均log +0.000130 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0756 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $112.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.89** / 初期 $100.00 (-1.11%)
- 確定: 195件 (Win 61 / Loss 107 / Flat 27) / pending 1件 / skip 224件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000259 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.89

## 6. Latest Market Context

- 更新: 2026-07-18T14:41:09.806311+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64132.8
- Funnel: target 885 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +37.83% | $77,449,502.38 |
| XEC/USDT:USDT | +26.51% | $4,238,912.87 |
| TRADOOR/USDT:USDT | +21.49% | $5,612,927.75 |
| B/USDT:USDT | +19.11% | $22,570,060.92 |
| ALLO/USDT:USDT | +17.95% | $6,530,177.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XEC/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |
| ALLO/USDT:USDT | below_1h_threshold | +1.90% | +1.82% |
| JASMY/USDT:USDT | below_1h_threshold | +1.78% | +1.70% |
| RAVE/USDT:USDT | below_1h_threshold | +1.66% | +1.58% |
| BSB/USDT:USDT | below_1h_threshold | +0.91% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
