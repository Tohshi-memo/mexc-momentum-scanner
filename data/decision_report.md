# Decision Report

- generated_at: 2026-07-18T12:11:18.933024+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8942**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8942, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.02% | **+0.51%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.39% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.24% | **+1.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.24% | **+0.99%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.49% | **+0.74%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.30% | **+0.65%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.06% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2454件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.92** / 初期 $100.00 (+11.92%)
- 確定: 903件 (Win 217 / Loss 182 / Flat 504) / skip 1450件
- 成長率目線: 平均log +0.000125 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0686 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $111.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.90** / 初期 $100.00 (-1.10%)
- 確定: 192件 (Win 60 / Loss 105 / Flat 27) / pending 4件 / skip 222件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.90

## 6. Latest Market Context

- 更新: 2026-07-18T12:11:11.284167+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64099.1
- Funnel: target 885 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +50.43% | $10,691,399.96 |
| AKE/USDT:USDT | +45.57% | $73,584,828.95 |
| XEC/USDT:USDT | +28.86% | $3,775,198.16 |
| TRADOOR/USDT:USDT | +26.37% | $5,078,008.47 |
| ROAM/USDT:USDT | +14.25% | $1,007,383.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.61% | +2.51% |
| BANK/USDT:USDT | below_1h_threshold | +1.40% | +1.30% |
| SYN/USDT:USDT | below_1h_threshold | +1.12% | +1.02% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.59% |
| BSB/USDT:USDT | below_1h_threshold | +0.69% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
