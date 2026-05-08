# Decision Report

- generated_at: 2026-05-08T20:32:37.599066+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3821**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3821, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/17 | 41.2% | +1.16% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.34% | **+0.15%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.01% | **+0.01%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.19% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.99% | **+0.44%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.52% | **+0.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.27% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 190件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T20:32:34.551316+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80131.6
- Funnel: target 767 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CORE/USDT:USDT | +13.28% | $1,244,185.21 |
| SATO/USDT:USDT | +12.12% | $6,127,741.83 |
| COLLECT/USDT:USDT | +11.12% | $2,720,870.77 |
| ICP/USDT:USDT | +10.82% | $204,697,458.04 |
| RKLBSTOCK/USDT:USDT | +10.75% | $2,621,340.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +3.61% | +3.62% |
| JASMY/USDT:USDT | below_1h_threshold | +2.66% | +2.68% |
| ENA/USDT:USDT | below_1h_threshold | +2.53% | +2.55% |
| CORE/USDT:USDT | below_1h_threshold | +2.00% | +2.01% |
| OP/USDT:USDT | below_1h_threshold | +1.80% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
