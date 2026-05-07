# Decision Report

- generated_at: 2026-05-07T19:07:25.191683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3687**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3687, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.11% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.66% | **+2.93%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.49% | **+2.44%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.15% | **+2.28%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.73% | **+1.49%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.06** / 初期 $100.00 (+10.06%)
- 確定: 181件 (Win 48 / Loss 61 / Flat 72) / skip 67件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +2.62%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $110.06

## 4. Latest Market Context

- 更新: 2026-05-07T19:07:22.420088+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=80052.7
- Funnel: target 766 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +38.36% | $3,122,239.40 |
| SATO/USDT:USDT | +26.63% | $6,046,358.96 |
| JTO/USDT:USDT | +21.12% | $14,348,876.60 |
| NOT/USDT:USDT | +14.75% | $8,654,884.99 |
| DYDX/USDT:USDT | +12.71% | $6,912,960.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +2.54% | +2.67% |
| DYDX/USDT:USDT | below_1h_threshold | +0.86% | +0.99% |
| PLAY/USDT:USDT | below_1h_threshold | +0.84% | +0.98% |
| BSB/USDT:USDT | below_1h_threshold | +0.64% | +0.78% |
| LINEA/USDT:USDT | below_1h_threshold | +0.43% | +0.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
