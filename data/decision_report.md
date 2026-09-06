# Decision Report

- generated_at: 2026-09-06T22:56:22.527088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13847**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13847, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.40% | **-1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 10/20 | 50.0% | +5.17% | **+2.59%** |
| LIMIT_9PCT | 9/20 | 45.0% | +4.95% | **+2.23%** |
| LIMIT_7PCT | 11/20 | 55.0% | +3.31% | **+1.82%** |
| LIMIT_10PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT | 12/20 | 60.0% | +0.45% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.01% | **+0.85%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.27% | **+0.83%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$837.19** / 初期 $100.00 (+737.19%)
- 確定: 5127件 (Win 1538 / Loss 1680 / Flat 1909) / skip 5281件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $837.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2570件 (Win 717 / Loss 618 / Flat 1235) / skip 4688件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0380 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 2441件 (Win 727 / Loss 932 / Flat 782) / pending 5件 / skip 2874件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000242 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_8PCT` TP_HIT account +0.34% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-06T22:56:10.523417+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79985.5
- Funnel: target 1059 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +207.63% | $3,067,471.76 |
| XAN/USDT:USDT | +11.33% | $1,425,396.64 |
| TIA/USDT:USDT | +10.33% | $11,662,418.51 |
| LINK/USDT:USDT | +6.79% | $38,909,869.45 |
| DASH/USDT:USDT | +6.14% | $42,905,545.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +3.23% | +3.12% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.00% | +2.89% |
| UAI/USDT:USDT | below_1h_threshold | +1.95% | +1.85% |
| LINK/USDT:USDT | below_1h_threshold | +1.31% | +1.21% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.88% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
