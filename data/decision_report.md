# Decision Report

- generated_at: 2026-08-07T17:26:28.706928+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10737**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10737, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 5/20 | 25.0% | +0.88% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.05% | **+0.90%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.37% | **+0.24%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.08% | **+0.03%** |
| MARKET_LONG | 20/20 | 100.0% | -0.02% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3499件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.90** / 初期 $100.00 (+44.90%)
- 確定: 1462件 (Win 411 / Loss 342 / Flat 709) / skip 2686件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0149 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $144.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.24** / 初期 $100.00 (+18.24%)
- 確定: 1178件 (Win 380 / Loss 465 / Flat 333) / pending 4件 / skip 1034件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.24

## 6. Latest Market Context

- 更新: 2026-08-07T17:26:17.296910+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=64604.9
- Funnel: target 961 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +14.03% | $1,779,884.79 |
| ACE/USDT:USDT | +10.98% | $35,089,842.93 |
| BLESS/USDT:USDT | +10.57% | $55,971,965.38 |
| C98/USDT:USDT | +8.77% | $2,173,272.44 |
| HEI/USDT:USDT | +8.61% | $24,722,131.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| C98/USDT:USDT | below_1h_threshold | +3.88% | +4.15% |
| CYS/USDT:USDT | below_1h_threshold | +3.74% | +4.01% |
| XAI/USDT:USDT | below_1h_threshold | +3.39% | +3.66% |
| BEAT/USDT:USDT | below_1h_threshold | +2.43% | +2.70% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.53% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
