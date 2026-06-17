# Decision Report

- generated_at: 2026-06-17T19:53:14.631736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6964**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6964, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +1.38% | **+0.52%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.05% | **-0.02%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.81% | **+3.61%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.82% | **+1.28%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.07% | **+0.86%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| ASK_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1817件 (Win 496 / Loss 573 / Flat 748) / skip 1708件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.20** / 初期 $100.00 (+3.20%)
- 確定: 237件 (Win 62 / Loss 57 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0630 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $103.20

## 5. Latest Market Context

- 更新: 2026-06-17T19:53:07.017574+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -2.08% price=64117.9
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +73.96% | $1,033,446.24 |
| SYN/USDT:USDT | +53.84% | $1,300,245.55 |
| MITO/USDT:USDT | +16.85% | $1,383,400.93 |
| RE/USDT:USDT | +14.85% | $1,657,658.91 |
| ESPORTS/USDT:USDT | +9.86% | $14,951,015.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.80% | +6.88% |
| PLAY/USDT:USDT | below_1h_threshold | +1.92% | +4.01% |
| UP/USDT:USDT | below_1h_threshold | +1.76% | +3.85% |
| TAC/USDT:USDT | below_1h_threshold | +1.19% | +3.27% |
| GUA/USDT:USDT | below_1h_threshold | +0.94% | +3.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
