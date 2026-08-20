# Decision Report

- generated_at: 2026-08-20T10:16:19.404666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12029**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12029, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_BB3S | 9/13 | 69.2% | -0.01% | **-0.00%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.87% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.91% | **+1.89%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.82% | **+1.53%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.94% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$600.15** / 初期 $100.00 (+500.15%)
- 確定: 4247件 (Win 1303 / Loss 1390 / Flat 1554) / skip 4343件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ETHFI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $600.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3619件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.76** / 初期 $100.00 (+16.76%)
- 確定: 1754件 (Win 520 / Loss 670 / Flat 564) / pending 3件 / skip 1745件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINIMAXSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.76

## 6. Latest Market Context

- 更新: 2026-08-20T10:16:10.889590+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.83% price=72373.4
- Funnel: target 1005 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +49.55% | $3,081,991.04 |
| BOME/USDT:USDT | +46.57% | $7,134,800.71 |
| MAGMA/USDT:USDT | +36.09% | $9,262,427.84 |
| USELESS/USDT:USDT | +24.50% | $1,978,441.30 |
| ORDI/USDT:USDT | +20.90% | $4,865,434.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +4.08% | +3.25% |
| BOME/USDT:USDT | below_1h_threshold | +2.76% | +1.94% |
| KORU/USDT:USDT | below_1h_threshold | +2.75% | +1.92% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.24% | +1.42% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.73% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
