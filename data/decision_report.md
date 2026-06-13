# Decision Report

- generated_at: 2026-06-13T18:25:30.772281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6598**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6598, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.08%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.89% | **+1.45%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.62** / 初期 $100.00 (+68.62%)
- 確定: 1471件 (Win 395 / Loss 466 / Flat 610) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $168.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.22** / 初期 $100.00 (+0.22%)
- 確定: 9件 (Win 3 / Loss 2 / Flat 4) / skip 0件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0677 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $100.22

## 5. Latest Market Context

- 更新: 2026-06-13T18:25:25.556782+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=64096.6
- Funnel: target 770 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +24.85% | $63,791,289.22 |
| AT/USDT:USDT | +12.64% | $1,014,361.17 |
| RIF/USDT:USDT | +9.32% | $6,364,566.28 |
| NOT/USDT:USDT | +3.79% | $2,715,721.87 |
| COAI/USDT:USDT | +3.71% | $24,166,808.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.32% | +4.07% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.98% | +1.74% |
| JCT/USDT:USDT | below_1h_threshold | +1.77% | +1.52% |
| CHZ/USDT:USDT | below_1h_threshold | +1.39% | +1.14% |
| EDGE/USDT:USDT | below_1h_threshold | +1.35% | +1.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
