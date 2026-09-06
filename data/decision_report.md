# Decision Report

- generated_at: 2026-09-06T02:37:02.881740+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13788**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13788, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.57% | **+0.14%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 3/13 | 23.1% | -0.24% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.85% | **+1.20%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.09% | **+1.19%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.17% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$867.32** / 初期 $100.00 (+767.32%)
- 確定: 5094件 (Win 1529 / Loss 1661 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $867.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.68** / 初期 $100.00 (+90.68%)
- 確定: 2533件 (Win 707 / Loss 599 / Flat 1227) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0582 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $190.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.10** / 初期 $100.00 (+20.10%)
- 確定: 2405件 (Win 716 / Loss 912 / Flat 777) / pending 6件 / skip 2853件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000326 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $120.10

## 6. Latest Market Context

- 更新: 2026-09-06T02:36:50.139758+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79889.3
- Funnel: target 1050 → liquid 124 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +43.35% | $109,294,703.54 |
| UAI/USDT:USDT | +37.54% | $7,781,569.42 |
| BASECAT/USDT:USDT | +24.21% | $2,051,916.37 |
| FLOCK/USDT:USDT | +23.20% | $1,017,604.28 |
| MAGMA/USDT:USDT | +21.44% | $2,529,617.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +4.94% | +4.97% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.70% | +2.74% |
| CATI/USDT:USDT | below_1h_threshold | +1.87% | +1.90% |
| BULLA/USDT:USDT | below_1h_threshold | +1.39% | +1.42% |
| BCH/USDT:USDT | below_1h_threshold | +1.20% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
