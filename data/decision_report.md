# Decision Report

- generated_at: 2026-09-06T00:06:35.370546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13781**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13781, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.73% | **+0.22%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.87% | **+0.55%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.93% | **+0.51%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$861.15** / 初期 $100.00 (+761.15%)
- 確定: 5087件 (Win 1525 / Loss 1658 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $861.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.08** / 初期 $100.00 (+89.08%)
- 確定: 2526件 (Win 704 / Loss 597 / Flat 1225) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0421 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $189.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.93** / 初期 $100.00 (+19.93%)
- 確定: 2398件 (Win 712 / Loss 909 / Flat 777) / pending 6件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000277 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $119.93

## 6. Latest Market Context

- 更新: 2026-09-06T00:06:25.238842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=79843.3
- Funnel: target 1050 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +36.05% | $77,036,600.77 |
| BASECAT/USDT:USDT | +25.32% | $1,931,565.81 |
| SUSHI/USDT:USDT | +19.26% | $3,775,977.24 |
| 4/USDT:USDT | +19.10% | $21,470,318.31 |
| FLOCK/USDT:USDT | +16.96% | $1,014,474.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +3.23% | +3.17% |
| ARB/USDT:USDT | below_1h_threshold | +1.92% | +1.86% |
| TUT/USDT:USDT | below_1h_threshold | +1.71% | +1.66% |
| BLESS/USDT:USDT | below_1h_threshold | +1.48% | +1.42% |
| BULLA/USDT:USDT | below_1h_threshold | +1.27% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
