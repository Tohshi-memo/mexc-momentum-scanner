# Decision Report

- generated_at: 2026-10-24T11:11:16.735413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17360**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17360, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.65% | **+0.99%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.31% | **+0.59%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.81% | **+3.24%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.19% | **+2.72%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.51% | **+2.48%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.02% | **+2.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,352.66** / 初期 $100.00 (+1252.66%)
- 確定: 6613件 (Win 1913 / Loss 2105 / Flat 2595) / skip 7308件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,352.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3930件 (Win 1083 / Loss 920 / Flat 1927) / skip 6841件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1229 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5517件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000439 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T11:11:04.443201+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80643.1
- Funnel: target 1079 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORDER/USDT:USDT | +138.81% | $5,060,047.78 |
| BMT/USDT:USDT | +52.52% | $2,152,260.90 |
| BIRB/USDT:USDT | +18.77% | $12,610,680.18 |
| NIL/USDT:USDT | +5.93% | $2,201,106.80 |
| IRYS/USDT:USDT | +5.13% | $102,881,919.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DNA/USDT:USDT | below_1h_threshold | +2.63% | +2.61% |
| BTW/USDT:USDT | below_1h_threshold | +0.65% | +0.63% |
| AXIS/USDT:USDT | below_1h_threshold | +0.58% | +0.56% |
| NIL/USDT:USDT | below_1h_threshold | +0.36% | +0.34% |
| WLFI/USDT:USDT | below_1h_threshold | +0.26% | +0.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
