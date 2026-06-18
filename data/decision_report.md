# Decision Report

- generated_at: 2026-06-18T05:39:25.142152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7010**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7010, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.38% | **+0.10%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.24% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$214.04** / 初期 $100.00 (+114.04%)
- 確定: 1856件 (Win 518 / Loss 587 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $214.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.64** / 初期 $100.00 (+5.64%)
- 確定: 283件 (Win 79 / Loss 74 / Flat 130) / skip 138件
- 成長率目線: 平均log +0.000194 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0637 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $105.64

## 5. Latest Market Context

- 更新: 2026-06-18T05:39:17.553883+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63862.8
- Funnel: target 793 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1, 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +96.48% | $36,551,120.20 |
| O/USDT:USDT | +58.32% | $2,252,933.33 |
| SYN/USDT:USDT | +56.21% | $4,799,126.71 |
| H/USDT:USDT | +34.56% | $32,504,598.74 |
| HOME/USDT:USDT | +31.83% | $1,851,194.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.57% | +4.55% |
| EVAA/USDT:USDT | below_1h_threshold | +4.25% | +4.24% |
| RE/USDT:USDT | below_1h_threshold | +3.20% | +3.18% |
| CLO/USDT:USDT | below_1h_threshold | +2.25% | +2.23% |
| UP/USDT:USDT | below_1h_threshold | +1.65% | +1.64% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
