# Decision Report

- generated_at: 2026-06-02T03:24:55.060062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5394**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5394, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.90% | **+1.24%** |
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.29% | **+0.25%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.17% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.76** / 初期 $100.00 (+31.76%)
- 確定: 907件 (Win 211 / Loss 272 / Flat 424) / skip 1048件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.17% 残高後 $131.76

## 4. Latest Market Context

- 更新: 2026-06-02T03:24:52.332327+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=70907.9
- Funnel: target 776 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +20.27% | $197,085,766.44 |
| ESPORTS/USDT:USDT | +19.76% | $10,803,327.14 |
| RIF/USDT:USDT | +19.54% | $1,187,347.82 |
| WLD/USDT:USDT | +16.15% | $136,153,189.76 |
| H/USDT:USDT | +16.03% | $56,144,645.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.42% | +4.29% |
| LAB/USDT:USDT | below_1h_threshold | +3.98% | +3.85% |
| RIF/USDT:USDT | below_1h_threshold | +3.50% | +3.38% |
| WLD/USDT:USDT | below_1h_threshold | +2.30% | +2.17% |
| INJ/USDT:USDT | below_1h_threshold | +2.19% | +2.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
