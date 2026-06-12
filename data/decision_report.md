# Decision Report

- generated_at: 2026-06-12T12:24:58.815527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6507**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6507, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.58% | **+0.63%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.49% | **+0.53%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.41% | **+0.25%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +4.87% | **+3.24%** |
| ASK_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.73** / 初期 $100.00 (+69.73%)
- 確定: 1380件 (Win 380 / Loss 444 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $169.73

## 4. Latest Market Context

- 更新: 2026-06-12T12:24:53.731922+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=63544.7
- Funnel: target 774 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +92.80% | $47,555,658.11 |
| VELVET/USDT:USDT | +89.80% | $156,371,229.31 |
| NAORIS/USDT:USDT | +49.21% | $5,394,332.63 |
| SKYAI/USDT:USDT | +42.40% | $16,816,032.04 |
| XPL/USDT:USDT | +40.80% | $13,846,392.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.59% | +4.88% |
| COAI/USDT:USDT | below_1h_threshold | +4.36% | +4.65% |
| AIN/USDT:USDT | below_1h_threshold | +3.14% | +3.43% |
| XPL/USDT:USDT | below_1h_threshold | +3.13% | +3.43% |
| UB/USDT:USDT | below_1h_threshold | +2.62% | +2.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
