# Decision Report

- generated_at: 2026-06-11T16:53:28.394116+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6378**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6378, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.18% | **+0.11%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.29% | **+0.10%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.01% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.17% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.13** / 初期 $100.00 (+51.13%)
- 確定: 1295件 (Win 332 / Loss 411 / Flat 552) / skip 1644件
- 成長率目線: 平均log +0.000319 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CHZ/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $151.13

## 4. Latest Market Context

- 更新: 2026-06-11T16:53:19.940404+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=62574.2
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +6.82% | $8,978,285.45 |
| SKYAI/USDT:USDT | +5.53% | $10,019,059.38 |
| SIREN/USDT:USDT | +4.96% | $5,843,386.02 |
| BILL/USDT:USDT | +4.79% | $2,341,173.45 |
| COLLECT/USDT:USDT | +4.18% | $2,514,867.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.79% | +5.03% |
| COLLECT/USDT:USDT | below_1h_threshold | +4.31% | +4.55% |
| ZBT/USDT:USDT | below_1h_threshold | +4.29% | +4.53% |
| VELVET/USDT:USDT | below_1h_threshold | +3.91% | +4.15% |
| LAB/USDT:USDT | below_1h_threshold | +3.79% | +4.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
