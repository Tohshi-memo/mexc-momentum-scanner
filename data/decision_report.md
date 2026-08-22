# Decision Report

- generated_at: 2026-08-22T02:01:20.695759+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12292**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12292, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.31% | **-2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.36% | **+0.27%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +4.82% | **+3.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.02% | **+2.72%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.62% | **+2.54%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.50% | **+2.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$697.73** / 初期 $100.00 (+597.73%)
- 確定: 4410件 (Win 1351 / Loss 1441 / Flat 1618) / skip 4443件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $697.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.02** / 初期 $100.00 (+55.02%)
- 確定: 1898件 (Win 523 / Loss 454 / Flat 921) / skip 3805件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2330 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $155.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.18** / 初期 $100.00 (+18.18%)
- 確定: 1841件 (Win 546 / Loss 695 / Flat 600) / pending 4件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000541 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.18

## 6. Latest Market Context

- 更新: 2026-08-22T02:01:10.121684+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77848.3
- Funnel: target 1018 → liquid 215 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +293.40% | $3,802,276.71 |
| CATE/USDT:USDT | +56.05% | $11,924,207.21 |
| AGI/USDT:USDT | +27.52% | $1,740,294.78 |
| ZEC/USDT:USDT | +23.48% | $300,902,899.29 |
| RE/USDT:USDT | +18.81% | $6,710,406.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPX/USDT:USDT | below_1h_threshold | +0.87% | +0.81% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +0.80% | +0.74% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +0.60% | +0.55% |
| SUI/USDT:USDT | below_1h_threshold | +0.55% | +0.50% |
| APE/USDT:USDT | below_1h_threshold | +0.54% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
