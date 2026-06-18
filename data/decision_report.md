# Decision Report

- generated_at: 2026-06-18T08:53:20.320214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7026**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7026, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.65% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.81% | **+0.40%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.95% | **+0.28%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.23% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$218.28** / 初期 $100.00 (+118.28%)
- 確定: 1872件 (Win 526 / Loss 595 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $218.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.30** / 初期 $100.00 (+6.30%)
- 確定: 299件 (Win 85 / Loss 81 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000204 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0701 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $106.30

## 5. Latest Market Context

- 更新: 2026-06-18T08:53:11.120118+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64429.3
- Funnel: target 793 → liquid 174 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +87.50% | $42,219,193.44 |
| O/USDT:USDT | +69.22% | $4,244,476.98 |
| SYN/USDT:USDT | +58.22% | $5,809,011.37 |
| HOME/USDT:USDT | +38.44% | $2,274,148.51 |
| H/USDT:USDT | +31.83% | $34,002,302.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MITO/USDT:USDT | below_1h_threshold | +3.83% | +3.90% |
| CHIP/USDT:USDT | below_1h_threshold | +3.76% | +3.82% |
| UP/USDT:USDT | below_1h_threshold | +3.05% | +3.12% |
| LAB/USDT:USDT | below_1h_threshold | +3.00% | +3.07% |
| HOME/USDT:USDT | below_1h_threshold | +2.70% | +2.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
