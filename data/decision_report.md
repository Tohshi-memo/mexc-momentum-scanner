# Decision Report

- generated_at: 2026-06-04T17:49:12.982142+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5653**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5653, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.66% | **+0.55%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.54** / 初期 $100.00 (-1.46%)
- 確定トレード: 98件 (TP 30 / SL 65 / EXP 3)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1207件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T17:49:07.208262+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.73% price=63069.5
- Funnel: target 771 → liquid 171 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%, rsi_15m 67%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +24.55% | $2,755,822.29 |
| LAB/USDT:USDT | +23.87% | $147,207,370.21 |
| PORTAL/USDT:USDT | +10.87% | $2,967,365.35 |
| HOME/USDT:USDT | +10.65% | $3,829,047.10 |
| ALLO/USDT:USDT | +8.02% | $5,701,284.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.11% | +3.83% |
| MEME/USDT:USDT | below_1h_threshold | +3.01% | +3.74% |
| MONAD/USDT:USDT | below_1h_threshold | +2.80% | +3.53% |
| GRASS/USDT:USDT | below_1h_threshold | +2.75% | +3.48% |
| BEAT/USDT:USDT | below_1h_threshold | +2.49% | +3.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
