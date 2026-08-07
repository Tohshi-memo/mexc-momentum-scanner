# Decision Report

- generated_at: 2026-08-07T20:56:24.637245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10758**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10758, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +6.62% | **+1.66%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.09% | **+0.20%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.74% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.46% | **+0.73%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3520件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.41** / 初期 $100.00 (+44.41%)
- 確定: 1478件 (Win 416 / Loss 346 / Flat 716) / skip 2691件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0401 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $144.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.43** / 初期 $100.00 (+18.43%)
- 確定: 1180件 (Win 381 / Loss 466 / Flat 333) / pending 2件 / skip 1050件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $118.43

## 6. Latest Market Context

- 更新: 2026-08-07T20:56:15.209286+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64941.9
- Funnel: target 961 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +86.51% | $2,131,861.24 |
| BLESS/USDT:USDT | +24.20% | $69,191,986.90 |
| EPIC/USDT:USDT | +16.96% | $2,113,124.31 |
| GWEI/USDT:USDT | +9.69% | $1,458,468.90 |
| SLX/USDT:USDT | +8.55% | $1,147,974.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.74% | +3.73% |
| SLX/USDT:USDT | below_1h_threshold | +3.28% | +3.27% |
| GWEI/USDT:USDT | below_1h_threshold | +3.27% | +3.26% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.92% | +2.91% |
| KORU/USDT:USDT | below_1h_threshold | +2.84% | +2.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
