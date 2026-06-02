# Decision Report

- generated_at: 2026-06-02T06:03:07.468144+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5411**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5411, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.86% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -1.02% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.19% | **+2.08%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.57% | **+1.93%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.00% | **+1.10%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.51% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.62** / 初期 $100.00 (+34.62%)
- 確定: 923件 (Win 216 / Loss 274 / Flat 433) / skip 1049件
- 成長率目線: 平均log +0.000322 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $134.62

## 4. Latest Market Context

- 更新: 2026-06-02T06:03:05.073512+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=70344.2
- Funnel: target 777 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +51.36% | $7,939,545.38 |
| US/USDT:USDT | +28.38% | $1,002,073.56 |
| ESPORTS/USDT:USDT | +25.71% | $11,601,861.99 |
| LAB/USDT:USDT | +22.08% | $209,102,264.47 |
| H/USDT:USDT | +21.64% | $54,792,421.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.24% | +2.08% |
| SLX/USDT:USDT | below_1h_threshold | +1.82% | +1.67% |
| UB/USDT:USDT | below_1h_threshold | +1.42% | +1.26% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.15% | +1.00% |
| EPIC/USDT:USDT | below_1h_threshold | +1.00% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
