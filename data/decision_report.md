# Decision Report

- generated_at: 2026-05-13T12:18:08.709995+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4221**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4221, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | -0.31% | **-0.31%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.64% | **-0.33%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.85% | **-0.37%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | -1.56% | **-0.39%** |
| LIMIT_8PCT | 4/20 | 20.0% | -2.07% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.20% | **+0.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.73% | **+0.66%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 441件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T12:18:05.331487+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80514.0
- Funnel: target 765 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +35.42% | $125,903,650.25 |
| INJ/USDT:USDT | +24.39% | $146,873,517.87 |
| COS/USDT:USDT | +23.77% | $1,770,247.38 |
| UB/USDT:USDT | +23.43% | $9,828,066.13 |
| TRUTH/USDT:USDT | +19.00% | $3,206,964.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +1.76% | +1.69% |
| UP/USDT:USDT | below_1h_threshold | +1.61% | +1.54% |
| RIVER/USDT:USDT | below_1h_threshold | +1.53% | +1.46% |
| IRYS/USDT:USDT | below_1h_threshold | +1.45% | +1.38% |
| EDU/USDT:USDT | below_1h_threshold | +1.15% | +1.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
