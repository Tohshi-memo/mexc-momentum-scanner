# Decision Report

- generated_at: 2026-05-13T13:48:08.690577+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4225**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4225, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.09% | **+0.09%** |
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |
| LIMIT_BB3S | 9/19 | 47.4% | -0.48% | **-0.23%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.38% | **-0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.49% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.59% | **+0.39%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 445件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T13:48:00.736623+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.71% price=79590.3
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +37.36% | $134,011,980.35 |
| COS/USDT:USDT | +30.45% | $1,816,315.26 |
| TRUTH/USDT:USDT | +28.61% | $3,715,300.04 |
| UB/USDT:USDT | +27.59% | $10,378,340.33 |
| JCT/USDT:USDT | +25.55% | $1,079,513.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +2.73% | +3.44% |
| UB/USDT:USDT | below_1h_threshold | +2.42% | +3.13% |
| MITO/USDT:USDT | below_1h_threshold | +2.13% | +2.84% |
| SATO/USDT:USDT | below_1h_threshold | +1.66% | +2.37% |
| BANANAS31/USDT:USDT | below_1h_threshold | +0.89% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
