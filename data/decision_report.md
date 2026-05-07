# Decision Report

- generated_at: 2026-05-07T14:37:34.893476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3643**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3643, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.67% | **-0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.98% | **+2.19%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.79% | **+2.08%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.19% | **+2.08%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +5.00% | **+2.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.20** / 初期 $100.00 (+11.20%)
- 確定: 137件 (Win 44 / Loss 50 / Flat 43) / skip 67件
- 成長率目線: 平均log +0.000775 / 幾何平均 +0.078% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $111.20

## 4. Latest Market Context

- 更新: 2026-05-07T14:37:31.587659+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=80109.6
- Funnel: target 771 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +92.52% | $10,932,956.85 |
| PENGUIN/USDT:USDT | +86.81% | $4,224,596.28 |
| SATO/USDT:USDT | +79.91% | $3,598,107.63 |
| DOGS/USDT:USDT | +48.56% | $17,596,775.99 |
| NIL/USDT:USDT | +47.30% | $4,630,850.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.63% | +5.07% |
| SATO/USDT:USDT | below_1h_threshold | +4.05% | +4.49% |
| NGAS/USDT:USDT | below_1h_threshold | +3.41% | +3.85% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.65% | +3.08% |
| JTO/USDT:USDT | below_1h_threshold | +2.40% | +2.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
