# Decision Report

- generated_at: 2026-06-18T09:14:00.444061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7029**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7029, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.79% | **+0.55%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.38% | **+1.10%** |
| ASK_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.56% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$221.19** / 初期 $100.00 (+121.19%)
- 確定: 1875件 (Win 529 / Loss 595 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $221.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.55** / 初期 $100.00 (+7.55%)
- 確定: 302件 (Win 88 / Loss 81 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0970 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $107.55

## 5. Latest Market Context

- 更新: 2026-06-18T09:13:54.408896+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64344.1
- Funnel: target 793 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +90.81% | $41,764,757.93 |
| O/USDT:USDT | +69.30% | $4,319,164.25 |
| SYN/USDT:USDT | +61.12% | $5,885,705.86 |
| HOME/USDT:USDT | +40.00% | $2,305,188.11 |
| H/USDT:USDT | +30.35% | $33,588,281.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +4.67% | +4.71% |
| LAB/USDT:USDT | below_1h_threshold | +4.32% | +4.36% |
| CLO/USDT:USDT | below_1h_threshold | +2.35% | +2.39% |
| GUA/USDT:USDT | below_1h_threshold | +2.17% | +2.21% |
| BSB/USDT:USDT | below_1h_threshold | +2.14% | +2.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
