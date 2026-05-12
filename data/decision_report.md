# Decision Report

- generated_at: 2026-05-12T16:47:59.300711+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4145**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4145, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.96% | **+1.56%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.91% | **+0.59%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.65** / 初期 $100.00 (+19.65%)
- 確定: 281件 (Win 80 / Loss 96 / Flat 105) / skip 425件
- 成長率目線: 平均log +0.000638 / 幾何平均 +0.064% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.65

## 4. Latest Market Context

- 更新: 2026-05-12T16:47:55.719547+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=79930.1
- Funnel: target 763 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1, 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +19.58% | $2,593,097.97 |
| UP/USDT:USDT | +8.47% | $1,750,462.61 |
| IRYS/USDT:USDT | +4.30% | $2,010,471.49 |
| XNY/USDT:USDT | +3.94% | $1,333,103.15 |
| GUA/USDT:USDT | +3.42% | $4,070,657.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +4.30% | +4.77% |
| XNY/USDT:USDT | below_1h_threshold | +3.95% | +4.41% |
| GUA/USDT:USDT | below_1h_threshold | +3.43% | +3.89% |
| COAI/USDT:USDT | below_1h_threshold | +2.83% | +3.30% |
| GIGA/USDT:USDT | below_1h_threshold | +2.75% | +3.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
