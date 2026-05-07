# Decision Report

- generated_at: 2026-05-07T02:27:16.979036+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3532**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3532, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.23% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.35% | **+1.76%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.12% | **+1.71%** |
| MARKET_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| ASK_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.65% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$100.62** / 初期 $100.00 (+0.62%)
- 確定: 27件 (Win 8 / Loss 11 / Flat 8) / skip 66件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $100.62

## 4. Latest Market Context

- 更新: 2026-05-07T02:27:10.751740+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=80853.7
- Funnel: target 770 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1, 4h RSI 81.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +157.72% | $1,085,459.24 |
| DOGS/USDT:USDT | +62.61% | $7,471,840.09 |
| PENGUIN/USDT:USDT | +37.17% | $1,091,102.83 |
| FHE/USDT:USDT | +27.33% | $15,940,426.79 |
| LAB/USDT:USDT | +14.16% | $257,644,100.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.80% | +4.13% |
| ORCA/USDT:USDT | below_1h_threshold | +2.57% | +2.90% |
| AR/USDT:USDT | below_1h_threshold | +2.03% | +2.36% |
| LAB/USDT:USDT | below_1h_threshold | +1.80% | +2.13% |
| BLESS/USDT:USDT | below_1h_threshold | +1.13% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
