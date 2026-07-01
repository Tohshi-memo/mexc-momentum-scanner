# Decision Report

- generated_at: 2026-07-01T15:24:33.254219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7998**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7998, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.83% | **-1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.47% | **+0.65%** |
| LIMIT_8PCT | 2/20 | 10.0% | +6.03% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.40% | **-0.04%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.10% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.96% | **+1.33%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |
| ASK_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.60% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$269.40** / 初期 $100.00 (+169.40%)
- 確定: 2396件 (Win 730 / Loss 792 / Flat 874) / skip 2163件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $269.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.58** / 初期 $100.00 (+6.58%)
- 確定: 517件 (Win 130 / Loss 123 / Flat 264) / skip 892件
- 成長率目線: 平均log +0.000123 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0313 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.58

## 5. Latest Market Context

- 更新: 2026-07-01T15:24:28.423137+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.49% price=60409.3
- Funnel: target 825 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +87.28% | $17,187,289.71 |
| M/USDT:USDT | +70.91% | $7,216,921.06 |
| ZBT/USDT:USDT | +28.30% | $3,393,425.47 |
| BASED/USDT:USDT | +24.70% | $14,983,254.25 |
| BTW/USDT:USDT | +21.57% | $6,291,296.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.35% | +2.86% |
| M/USDT:USDT | below_1h_threshold | +4.09% | +2.60% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +3.65% | +2.16% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.07% | +1.58% |
| BESTOCK/USDT:USDT | below_1h_threshold | +3.04% | +1.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
