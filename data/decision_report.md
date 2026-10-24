# Decision Report

- generated_at: 2026-10-24T12:36:26.530933+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17363**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17363, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_9PCT | 4/20 | 20.0% | +7.15% | **+1.43%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.59% | **+1.29%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.65% | **+0.99%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.58% | **+3.22%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +4.80% | **+2.88%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.66% | **+2.56%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,372.94** / 初期 $100.00 (+1272.94%)
- 確定: 6616件 (Win 1915 / Loss 2106 / Flat 2595) / skip 7308件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,372.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3930件 (Win 1083 / Loss 920 / Flat 1927) / skip 6844件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1681 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5521件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000500 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T12:36:13.969422+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=80761.2
- Funnel: target 1079 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORDER/USDT:USDT | +108.63% | $7,002,686.60 |
| BMT/USDT:USDT | +48.71% | $2,274,528.89 |
| BIRB/USDT:USDT | +25.60% | $13,084,245.70 |
| NIL/USDT:USDT | +4.90% | $2,346,616.09 |
| AGT/USDT:USDT | +4.66% | $10,636,663.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDER/USDT:USDT | below_1h_threshold | +2.09% | +1.85% |
| BMT/USDT:USDT | below_1h_threshold | +1.67% | +1.42% |
| AXIS/USDT:USDT | below_1h_threshold | +0.50% | +0.26% |
| NIL/USDT:USDT | below_1h_threshold | +0.32% | +0.08% |
| NGAS/USDT:USDT | below_1h_threshold | +0.30% | +0.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
