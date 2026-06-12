# Decision Report

- generated_at: 2026-06-12T05:51:00.835496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6469**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6469, expectancy=-0.07%
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
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.35% | **+0.41%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.35% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.38% | **+2.38%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.39% | **+2.03%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.01% | **+1.96%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +3.24% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$160.74** / 初期 $100.00 (+60.74%)
- 確定: 1344件 (Win 358 / Loss 430 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $160.74

## 4. Latest Market Context

- 更新: 2026-06-12T05:50:53.141475+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=63336.8
- Funnel: target 783 → liquid 155 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +69.06% | $142,754,054.66 |
| H/USDT:USDT | +38.93% | $41,826,400.21 |
| NAORIS/USDT:USDT | +33.15% | $1,863,452.77 |
| ESPORTS/USDT:USDT | +32.54% | $31,810,724.32 |
| XPL/USDT:USDT | +29.83% | $6,782,146.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.97% | +5.50% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.34% | +4.86% |
| XMR/USDT:USDT | below_1h_threshold | +4.10% | +4.62% |
| FHE/USDT:USDT | below_1h_threshold | +3.31% | +3.84% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.73% | +3.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
