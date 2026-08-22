# Decision Report

- generated_at: 2026-08-22T03:26:30.728255+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12300**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12300, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.09% | **-2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +5.42% | **+5.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.03% | **+2.73%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.71% | **+2.23%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.40% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$704.91** / 初期 $100.00 (+604.91%)
- 確定: 4418件 (Win 1353 / Loss 1442 / Flat 1623) / skip 4443件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $704.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.09** / 初期 $100.00 (+56.09%)
- 確定: 1906件 (Win 525 / Loss 455 / Flat 926) / skip 3805件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2655 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $156.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.59** / 初期 $100.00 (+18.59%)
- 確定: 1848件 (Win 548 / Loss 696 / Flat 604) / pending 6件 / skip 1928件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000616 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.59

## 6. Latest Market Context

- 更新: 2026-08-22T03:26:21.351165+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=78676.9
- Funnel: target 1018 → liquid 219 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.3 >= 65=1, 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +256.70% | $4,071,283.78 |
| CATE/USDT:USDT | +72.90% | $11,859,459.04 |
| DASH/USDT:USDT | +33.22% | $14,568,832.32 |
| AGI/USDT:USDT | +28.98% | $1,823,719.95 |
| MUBARAK/USDT:USDT | +27.95% | $1,225,226.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_relative_strength | +5.15% | +4.88% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +4.05% | +3.78% |
| WIF/USDT:USDT | below_1h_threshold | +3.59% | +3.33% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.21% | +2.94% |
| DOGE/USDT:USDT | below_1h_threshold | +2.98% | +2.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
