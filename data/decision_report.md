# Decision Report

- generated_at: 2026-05-13T10:03:26.066140+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4212**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4212, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | -0.64% | **-0.26%** |
| ASK | 20/20 | 100.0% | -0.26% | **-0.26%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.64% | **-0.33%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.85% | **-0.37%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | -2.00% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.37% | **+1.19%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.37% | **+0.89%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 432件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T10:03:22.547427+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=81190.3
- Funnel: target 765 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +42.67% | $1,630,736.98 |
| LAB/USDT:USDT | +29.28% | $110,533,601.00 |
| INJ/USDT:USDT | +26.67% | $90,676,281.65 |
| SATO/USDT:USDT | +24.32% | $1,281,527.89 |
| UB/USDT:USDT | +21.23% | $6,821,168.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COS/USDT:USDT | below_1h_threshold | +1.51% | +1.58% |
| B/USDT:USDT | below_1h_threshold | +1.18% | +1.26% |
| FF/USDT:USDT | below_1h_threshold | +1.17% | +1.25% |
| IRYS/USDT:USDT | below_1h_threshold | +0.68% | +0.75% |
| INJ/USDT:USDT | below_1h_threshold | +0.58% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
