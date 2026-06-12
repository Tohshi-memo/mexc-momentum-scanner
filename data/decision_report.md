# Decision Report

- generated_at: 2026-06-12T06:52:39.870982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6476**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6476, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +3.20% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.25% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| ASK_LONG | 20/20 | 100.0% | +2.09% | **+2.09%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.03% | **+1.42%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +3.92% | **+1.37%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.06% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.15** / 初期 $100.00 (+63.15%)
- 確定: 1351件 (Win 363 / Loss 432 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000362 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $163.15

## 4. Latest Market Context

- 更新: 2026-06-12T06:52:30.254847+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.61% price=62933.0
- Funnel: target 783 → liquid 155 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1, 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +94.75% | $142,423,118.94 |
| ESPORTS/USDT:USDT | +48.53% | $33,503,976.30 |
| H/USDT:USDT | +39.71% | $44,023,772.51 |
| NAORIS/USDT:USDT | +33.56% | $2,092,740.84 |
| XPL/USDT:USDT | +29.82% | $7,157,833.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +3.54% | +4.15% |
| COAI/USDT:USDT | below_1h_threshold | +2.49% | +3.10% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.44% | +3.06% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.45% | +2.06% |
| STG/USDT:USDT | below_1h_threshold | +1.41% | +2.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
