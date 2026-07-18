# Decision Report

- generated_at: 2026-07-18T23:41:11.363883+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8985**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8985, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.35% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.26% | **+1.93%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.99% | **+1.80%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.79% | **+1.68%** |
| MARKET_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.72% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2497件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 946件 (Win 236 / Loss 191 / Flat 519) / skip 1450件
- 成長率目線: 平均log +0.000196 / 幾何平均 +0.020% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2032 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $120.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定: 196件 (Win 62 / Loss 107 / Flat 27) / pending 0件 / skip 258件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000570 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $99.04

## 6. Latest Market Context

- 更新: 2026-07-18T23:41:06.884756+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64786.0
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +55.53% | $28,722,325.40 |
| BANK/USDT:USDT | +41.40% | $18,882,603.79 |
| TLM/USDT:USDT | +28.54% | $2,403,170.69 |
| B/USDT:USDT | +18.65% | $31,542,415.49 |
| AKE/USDT:USDT | +17.10% | $82,015,308.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.54% | +3.53% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.08% | +2.07% |
| BANK/USDT:USDT | below_1h_threshold | +1.70% | +1.68% |
| TAG/USDT:USDT | below_1h_threshold | +1.09% | +1.07% |
| JASMY/USDT:USDT | below_1h_threshold | +1.08% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
